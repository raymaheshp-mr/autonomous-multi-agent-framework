import streamlit as st

st.set_page_config(
    page_title = 'Homepage',
    layout="wide"
)
st.html("""
    <style>
       

        ol {
            padding-left: 40px;
        }
    </style>
    """
)


st.title('Autonomous Multi-Agent Framework')
st.subheader("*powered by IBM watsonx*", divider="gray")

set1info = '''
<h4>Problem Statement: Limitations of Non-Autonomous Agentic Framework</h4>

Agentic frameworks have greatly complemented Generative AI by enhancing its creativity, problem-solving capabilities, adaptability and efficiency. However, a non-autonomous agentic framework lacks the ability to make independent decisions or take actions without explicit instructions. Following are some of the major limitations.
<ol>
    <li><b>Lack of Flexibility:</b> As they follow pre-defined rules and instructions, hence they work within a boundary and lack the ability to initiate actions on their own.</li>
    <li><b>Dependency on External Input:</b> Performance of these agents is affected if the user’s input is unclear, incorrect, incomplete or delayed.</li>
    <li><b>Limited Creativity:</b> These agents might struggle with tasks that require creative problem-solving as they operate within the constraints of pre-defined rules and instructions.</li>
    <li><b>Limited Personalization:</b> Without autonomy, these agents may struggle to provide highly personalized experiences. They can't actively gather and utilize user-specific information to tailor their responses.</li>
    <li><b>Limited Generalization:</b> These agents may struggle to generalize knowledge from one domain to another, as they lack the autonomy to explore and learn from new environments.</li>
</ol>
Several multi-agent frameworks are available in the industry like CrewAI, LangGraph and IBM’s BeeAI. These frameworks provide different architectures for implementing multi-agent based applications, but none of them provides a fully autonomous agent.

<h4>Solution: Autonomous Multi-Agent Framework powered by IBM Watsonx</h4>

This integrated framework leverages IBM watsonx's Generative AI capabilities to enable dynamic creation of autonomous worker agents based on business profiles and business rules. In our approach, a sophisticated multi-agent framework, emerges as a singular, autonomous Master Agent that orchestrates the creation of worker agents and tasks at runtime to achieve the business objectives. Our approach uses CrewAI framework as the base to implement our framework. The same approach can be extended to other frameworks.

'''
set2info = '''
<h4>Key Components</h4>
<ol>
    <li><b>Master Agent Development:</b> The Master Agent analyses and extracts objectives from user-provided business requirements and rules, decomposes those objectives into steps and creates an execution plan.</li>
    <li><b>Agent Creation:</b> The Master Agent dynamically creates worker agents at runtime based on the decomposed steps, generating details such as role, goal, and backstory for each worker agent.</li>
    <li><b>Task Generation:</b> The Master Agent analyses the specifics of the assignment given to each worker agent, based on which it allocates tasks with descriptions and the expected output.</li>
    <li><b>Tool Calling:</b> The Master agent evaluates if the worker agents are self-sufficient to execute the task or they require external assistance. If deemed required, relevant tools are automatically selected from the Toolkit Library and instantiated and assigned to the agents for execution.</li>
    <li><b>Collaboration:</b> Through callback mechanism the Master Agent monitors the execution of the worker agents and enables sharing of information between worker agents ensuring successful execution of the entire operation.</li>
</ol>

<h4>Autonomous Multi-Agent Framework Governance</h4>
Although not a part of the prototype, but this framework proposes a robust governance framework which can both monitor and evaluate the swanned agents. The governance module can utilize the capabilities of watsonx.governance and also infuse custom capabilities of opensource libraries like AgentBench, AgentOps, CAMEL, etc. The governance module can handle unique challenges like cascading failures, emergent misalignments, and toolchain misuse which would require dynamic, identity-centric access controls and continuous performance monitoring.
<ol>
    <li><b>Monitoring:</b> The framework calls for continuous, real time insight into the health, performance, and risk profile of autonomous AI agents as they carry out end to end workflows. It outlines the following metrics for agent monitoring.
        <ul>
			<li> <b>Journey completion rate:</b> percentage of end-to-end agent workflows that meet defined success criteria under orchestration.</li>
			<li> <b>Task adherence:</b> how consistently an agent follows the stated goal and constraints across steps in a plan.</li>
			<li> <b>Intent resolution:</b> correctness of interpreting user intent and mapping it to the right plan or tools in context.</li>
			<li> <b>Tool call accuracy</b> share of tool invocations that are both syntactically valid and semantically correct for the task.</li>
			<li> <b>Answer quality</b> relevance, faithfulness, and similarity to ground truth for outputs across domains and datasets.</li>
			<li> <b>Retrieval quality</b> context relevance, precision, hit rate, reciprocal rank, average precision, and NDCG for RAG pipelines.</li>
			<li> <b>Safety risk</b> PII exposure, harm, bias, profanity, sexual content, jailbreak, and prompt safety risk scores to gate unsafe actions.</li>
			<li> <b>Reliability and latency</b> response times, failures, and trace completeness observed via telemetry to maintain SLOs.</li>
			<li> <b>Cost and throughput</b> interaction duration, token counts, and cost per task for capacity planning and ROI analysis.</li>
        </ul>
    </li>
    <li><b>Evaluation:</b> The framework calls for regular, in depth evaluations of how effectively agents achieve business objectives, adhere to safety standards, and satisfy operational expectations. It defines the following metrics for agent evaluation.
        <ul>
			<li> <b>Task effectiveness</b> journey completion rate, task adherence, and intent resolution quantify whether agents achieve goals and follow instructions.</li>
			<li> <b>Tool-use quality</b> tool call accuracy and syntactic validity ensure correct API selection and parameterization within multi-step plans.</li>
			<li> <b>Answer quality</b> relevance, faithfulness, and similarity measure the correctness and grounding of generated responses with or without ground truth.</li>
			<li> <b>Retrieval quality (RAG)</b> context relevance, precision, hit rate, reciprocal rank, average precision, and NDCG capture the usefulness of retrieved evidence.</li>
			<li> <b>Safety and compliance</b> PII risk, harm, bias, profanity, sexual content, jailbreak, and prompt safety risk quantify content and behavioural risks.</li>
			<li> <b>Observability and reliability</b> latency, failures, response time distributions, and trace completeness track runtime health and performance at scale.</li>
			<li> <b>Business and cost</b> interaction duration, token counts, and cost per task enable ROI, throughput, and capacity planning in production.</li>
        </ul>
    </li>
</ol>

<h4>Embracing the Future with Autonomous Agents</h4>

This autonomous multi-agent framework can boost enterprise productivity and efficiency by streamlining processes, freeing up human workers for strategic tasks, and reducing costs. It can also enhance decision-making by analysing patterns and trends, and scale with your enterprise as it grows and adapts to changing demands.

<h4>Role of watsonx.ai</h4>

We have leveraged multiple capabilities and features of IBM watsonx.ai to build this autonomous multi-agent framework. Here is a detailed overview of the key components and integrations:
<ol>
    <li><b>Prompt Lab:</b> Custom prompts are crafted in the Prompt Lab using the "granite-3-2-8b-instruct" model. This enables the dynamic creation of autonomous worker agents, tasks, and identification of tools based on the business profile and business rules provided as input by the user. The Prompt Lab facilitates the generation of highly tailored and contextually relevant prompts, ensuring that the agents are well-equipped to handle specific business needs.</li>
    <li><b>IBM watsonx.ai and CrewAI Integration:</b> The multi-agent framework, comprising dynamic agents, tasks, in-built tools, and custom tools, is built, orchestrated, and executed using CrewAI in integration with IBM watsonx.ai's "granite-3-2-8b-instruct" model. This model supports enhanced reasoning capabilities, making it ideal for creating autonomous agents with configurable thinking capabilities. This means the reasoning can be controlled and applied as needed, ensuring optimal performance and adaptability.</li>
    <li><b>Prompt Executing & LLM Inferencing:</b> The watsonx.ai Runtime service offered by IBM watsonx.ai is used to execute the designed prompts as well as the crew. This service ensures seamless execution and integration, allowing the agents to perform their tasks efficiently and effectively.</li>
    <li><b>watsonx.ai Studio:</b> IBM watsonx.ai provides a studio where we can design and implement our solutions. We have extensively used Jupyter notebooks to develop our application code and test the outcomes before deployment.</li>
</ol>
By leveraging these advanced capabilities, we have created a robust and adaptable multi-agent framework that can dynamically respond to various business needs, ensuring enhanced efficiency and effectiveness in task execution.

<h4>Live Demo</h4>

We have provided implementation of two different use cases using the Autonomous Multi-Agent framework. The details of the two use cases are:
<ol>
    <li><b>Smart Assistant Test Automation:</b> This use case automates the testing of smart assistants.
        <ul>
        <li> It reads the folder to establish the knowledge base using the FileReadTool of CrewAI</li>
        <li> Generates questions which can be asked by users to the smart assistant.</li>
        <li> Since the same question can be asked in a different way by different users, hence it creates alternative questions.</li>
        <li> To assist the test manager to establish the ground truth, it generates alternative answers.</li>
        <li> It mimics a smart assistant and generates answers for the generated questions.</li>
        <li> Finally, it uses semantic similarity matching to evaluate the smart assistants’ answers with the ground truth to generate the test result.</li>
        </ul>
    </li>
    <li><b>Product Review System:</b> This use case performs analytics on customer reviews.
        <ul>
        <li> Fetches the product reviews from the provided link using a custom tool</li>
        <li> Classifies the review as Positive, Negative or Neutral</li>
        <li> Uses the positive reviews to generate the positive review summary</li>
        <li> Uses the negative reviews to generate the negative review summary</li>
        <li> Extracts product features from reviews and classifies them as positive or negative</li>
        <li> Generates a summarized product review</li>
        <li> Generates Search Engine Optimization (SEO) content</li>
        </ul>
    </li>
</ol>
In the same way other use case can also be experimented with by selecting “New Run” and providing use case name, business profile, business rules and input data.

'''
st.markdown(set1info, unsafe_allow_html=True)
st.image("architecture.png", caption="Architecture Diagram")
st.markdown(set3info, unsafe_allow_html=True)
