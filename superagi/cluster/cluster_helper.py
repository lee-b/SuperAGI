from superagi.cluster.cluster_prompt_builder import ClusterPromptBuilder
from superagi.helper.token_counter import TokenCounter
from superagi.llms.openai import OpenAi
from superagi.models.cluster import Cluster
from superagi.models.cluster_agent import ClusterAgent
from superagi.models.cluster_configuration import ClusterConfiguration
from superagi.models.configuration import Configuration
from superagi.models.organisation import Organisation


class ClusterHelper:
    @classmethod
    def get_tasks(cls, session, cluster_execution_id):
        cluster = Cluster.get_cluster_by_execution_id(
            session, cluster_execution_id)
        cluster_config = ClusterConfiguration.fetch_cluster_configuration(
            session, cluster)
        goals = cluster_config['goal']
        instructions = cluster_config['instruction']
        agents = ClusterAgent.get_cluster_agents_by_cluster_id(
            session, cluster.id)
        prompt_dict = ClusterPromptBuilder.initialize_tasks_prompt()
        prompt = ClusterPromptBuilder.replace_main_variables(
            prompt_dict["prompt"], goals, instructions, agents)
        tasks = cls._get_completion(session, prompt, cluster)
        tasks = eval(tasks)
        return tasks

    @classmethod
    def get_agent_for_task(cls, session, cluster_execution_id, task):
        cluster = Cluster.get_cluster_by_execution_id(
            session, cluster_execution_id)
        agents = ClusterAgent.get_cluster_agents_by_cluster_id(
            session, cluster.id)
        cluster_config = ClusterConfiguration.fetch_cluster_configuration(
            session, cluster)
        prompt_dict = ClusterPromptBuilder.decide_agent_prompt()
        prompt = ClusterPromptBuilder.replace_main_variables(
            prompt_dict["prompt"],
            cluster_config['goal'],
            cluster_config['instruction'],
            agents)
        prompt = ClusterPromptBuilder.replace_task_based_variables(
            prompt, task)
        response = cls._get_completion(session, prompt, cluster)
        response = eval(response)
        if response["agent"]:
            return agents[response["agent"]["index"] - 1].id
        return None

    @classmethod
    def _get_completion(cls, session, prompt, cluster):
        organisation = Organisation.get_organisation_by_project_id(
            session, cluster.project_id)
        cluster_config = ClusterConfiguration.fetch_cluster_configuration(
            session, cluster)
        model = cluster_config['model']
        messages = []
        message = {
            "role": "system",
            "content": prompt
        }
        messages.append(message)
        base_token_limit = TokenCounter.count_message_tokens(messages, model)
        llm = OpenAi(
            model=model,
            api_key=Configuration.fetch_configuration(
                session,
                organisation.id,
                "model_api_key"))
        token_limit = TokenCounter.token_limit(model)
        completion = llm.chat_completion(
            messages, token_limit - base_token_limit)
        return completion['content']
