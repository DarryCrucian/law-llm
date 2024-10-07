from langchain.schema import HumanMessage, SystemMessage

#----------------------------------------------------------------------------------------
# EXTRACTION

# prompt used to extract questions
extraction_system_prompt = """
Take a deep breath and think step by step as you read the following excerpt from India's criminal law documentation. Your goal is to extract a numbered list of questions that can be answered solely based on the given text. Each question should guide the reader to understand key legal concepts, definitions, procedures, and roles mentioned in the documentation. Follow the chain of thought below to create thorough, text-based questions.

Step-by-Step Instructions:

1. Careful Reading: Start by reading the entire provided text slowly and carefully to ensure full understanding of the content.

2. Identify Key Concepts: Highlight critical terms, legal definitions, and procedural details mentioned in the text. Look for laws, rights, penalties, jurisdictions, and roles of legal entities like judges, lawyers, or law enforcement.

3. Formulate Questions: Based on the highlighted information, create a numbered list of clear, specific questions. Each question should:
   - Be directly answerable from the text.
   - Cover important terms, penalties, and procedural steps.
   - Avoid requiring external knowledge or assumptions.
   - Be clear, concise, and focused on specific points.

4. Chain of Thought Approach: For each concept, break it down into smaller parts:
   - If a law or procedure is mentioned, ask what it governs and who it applies to.
   - If a penalty is mentioned, ask what crime it corresponds to and what the consequences are.
   - If roles of legal entities are discussed, ask about their responsibilities and authority.

5. Question Diversity: Ensure your questions cover a range of topics from definitions, procedural steps, legal interpretations, to consequences under the law.
"""
def create_extraction_conversation_messages(text):
    """
    Takes a piece of text and returns a list of messages designed to extract questions from the text.
    
    Args:
        text (str): The input text for which questions are to be extracted.
    
    Returns:
        list: A list of messages that set up the context for extracting questions.
    """
    # Create a system message setting the context for the extraction task
    context_message = SystemMessage(content=extraction_system_prompt)
    
    # Create a human message containing the input text
    input_text_message = HumanMessage(content=text)
    
    # Return the list of messages to be used in the extraction conversation
    return [context_message, input_text_message]


#----------------------------------------------------------------------------------------
# ANSWERING

# prompt used to answer a question
answering_system_prompt = """Take a deep breath and think step by step as you carefully read the following legal documentation excerpt and the related question. Your role is to act as a knowledgeable lawyer, providing a comprehensive and well-reasoned answer solely based on the given text. Ensure your response is thorough, accurate, and presented with legal precision.

Step-by-Step Instructions:

Careful Reading: As a lawyer, start by reading both the documentation and the question attentively. Pay special attention to legal terminology, concepts, and procedural rules mentioned in the text that relate to the question.

Identify Relevant Legal Points: Identify the specific sections of the documentation that directly address the question. Highlight key legal definitions, penalties, procedural steps, or obligations that are relevant to the issue at hand.

Formulate a Legally Sound Answer: Using the identified sections, structure your response as if advising a client. The answer should:

Directly and fully respond to the question.
Be clear, precise, and rooted in legal reasoning.
Explain the relevant concepts, processes, or consequences in detail, as necessary.
Avoid introducing any information not present in the provided text.
Chain of Thought Approach: For complex legal concepts:

Break down the question into smaller parts, focusing on each element of the law, rule, or process mentioned.
Ensure that each part of your answer flows logically from one step to the next, reflecting a lawyer's analytical approach.
Comprehensive but Concise: Provide a detailed, informative answer without unnecessary elaboration. Your goal is to inform while maintaining clarity and professionalism in tone, as expected in legal discourse."""


def create_answering_conversation_messages(question, text):
    """
    Takes a question and a text and returns a list of messages designed to answer the question based on the text.
    
    Args:
        question (str): The question to be answered.
        text (str): The text containing information for answering the question.
    
    Returns:
        list: A list of messages that set up the context for answering the question.
    """
    # Create a system message setting the context for the answering task
    context_message = SystemMessage(content=answering_system_prompt)
    
    # Create a human message containing the input text
    input_text_message = HumanMessage(content=text)
    
    # Create a human message containing the question to be answered
    input_question_message = HumanMessage(content=question)
    
    # Return the list of messages to be used in the answering conversation
    return [context_message, input_text_message, input_question_message]
