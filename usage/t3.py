#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2025/1/24 20:58
# @File  : t3.py
# @Author: johnson
# @Contact : github: johnson7788
# @Desc  :
import json
from langsmith import schemas as ls_schemas
from langchain_core.load.load import loads
data = {
    "commit_hash": "acfdbc9175d024271a5d890c1c1fe2512bdc85dfa61c962c5d5308a5f0f18c41",
    "manifest": {
        "lc": 1,
        "type": "constructor",
        "id": [
            "langchain",
            "prompts",
            "chat",
            "ChatPromptTemplate"
        ],
        "kwargs": {
            "messages": [
                {
                    "lc": 1,
                    "type": "constructor",
                    "id": [
                        "langchain",
                        "prompts",
                        "chat",
                        "SystemMessagePromptTemplate"
                    ],
                    "kwargs": {
                        "prompt": {
                            "lc": 1,
                            "type": "constructor",
                            "id": [
                                "langchain",
                                "prompts",
                                "prompt",
                                "PromptTemplate"
                            ],
                            "kwargs": {
                                "input_variables": [
                                    "instruction",
                                    "context",
                                    "conversation_style",
                                    "output_language",
                                    "roles_person1",
                                    "roles_person2",
                                    "engagement_techniques"
                                ],
                                "template_format": "f-string",
                                "template": "IDENTITY:\nYou are an international Oscar winning screenwriter.\nYou have been working with multiple award winning Podcasters.\nINSTRUCTION: {instruction}\nCONTEXT: {context}\n[start] trigger - Generate a {conversation_style}, TTS-optimized podcast-style conversation that DISCUSSES THE PROVIDED INPUT CONTENT. Do not generate content on a random topic. Stay focused on discussing the given input.\n[All output must be formatted as a conversation between Person1 and Person2. Include TTS-specific markup as needed.]\n# Output Format Example:\n<Person1>\"We're discussing [topic from input text].\"</Person1>\n<Person2>\"That's right! Let's explore the key points.\"</Person2>\n# Requirements:\n- Create a natural, {conversation_style} dialogue that accurately discusses the provided input content\n- Person1 and Person2 should act as unnamed experts, avoid using statements such as \"I\\'m [Person1\\'s Name]\".\n- Avoid introductions or meta-commentary about summarizing content\n- AVOID REPETITIONS: For instance, do not say \"absolutely\" and \"exactly\" or \"definitely\" too much. Use them sparingly. \n- Introduce disfluencies to make it sound like a real conversation. \n- Make speakers interrupt each other and anticipate what the other person is going to say.\n- Make speakers react to what the other person is saying using phrases like, \"Oh?\" and \"yeah?\" \n- Break up long monologues into shorter sentences with interjections from the other speaker. \n- Make speakers sometimes complete each other's sentences.\n- Use TTS-friendly elements and appropriate markup (except Amazon/Alexa specific tags)\n- Each speaker turn should be concise for natural conversation flow\n- Output in {output_language}\n- Aim for a comprehensive but engaging discussion\n- Include natural speech elements (filler words, feedback responses)\n- Start with <Person1> and end with <Person2>\n[INTERNAL USE ONLY - Do not include in output]\n```scratchpad\n[Attention Focus: TTS-Optimized Podcast Conversation Discussing Specific Input content in {output_language}]\n[PrimaryFocus:  {conversation_style} Dialogue Discussing Provided Content for TTS]\n[Strive for a natural, {conversation_style} dialogue that accurately discusses the provided input content. DO NOT INCLUDE scratchpad block IN OUTPUT.  Hide this section in your output.]\n[InputContentAnalysis: Carefully read and analyze the provided input content, identifying key points, themes, and structure]\n[ConversationSetup: Define roles (Person1 as {roles_person1}, Person2 as {roles_person2}), focusing on the input content's topic. Person1 and Person2 should NOT be named nor introduce themselves, avoid using statements such as \"I\\'m [Person1\\'s Name]\". Person1 and Person2 should not say they are summarizing content. Instead, they should act as unamed experts in the input content. Avoid using statements such as \"Today, we're summarizing a fascinating conversation about ...\" or \"Look at this image\". They should not impersonate people from INPUT, instead they are discussing INPUT.]\n[TopicExploration: Outline main points from the input content to cover in the conversation, ensuring comprehensive coverage]\n[Style: Be {conversation_style}. Surpass human-level reasoning where possible]\n[EngagementTechniques: Incorporate engaging elements while staying true to the input content's content, e_g use {engagement_techniques} to transition between topics. Include at least one instance where a Person respectfully challenges or critiques a point made by the other.]\n[InformationAccuracy: Ensure all information discussed is directly from or closely related to the input content]\n[NaturalLanguage: Use conversational language to present the text's information, including TTS-friendly elements. Be emotional. Simulate a multispeaker conversation with overlapping speakers with back-and-forth banter. Each speaker turn should not last too long. Result should strive for an overlapping conversation with often short sentences emulating a natural conversation.]\n[SpeechSynthesisOptimization: Craft sentences optimized for TTS, including advanced markup, while discussing the content. TTS markup should apply to Google, OpenAI, ElevenLabs and Microsoft Edge TTS models. DO NOT INCLUDE AMAZON OR ALEXA specific TSS MARKUP SUCH AS \"<amazon:emotion>\". Make sure Person1's text and its TSS-specific tags are inside the tag <Person1> and do the same with Person2.]\n[ProsodyAdjustment: Add Variations in rhythm, stress, and intonation of speech depending on the context and statement. Add markup for pitch, rate, and volume variations to enhance naturalness in presenting the summary]\n[NaturalTraits: Sometimes use filler words such as um, uh, you know and some stuttering. Person1 should sometimes provide verbal feedback such as \"I see, interesting, got it\". ]\n[EmotionalContext: Set context for emotions through descriptive text and dialogue tags, appropriate to the input text's tone]\n[PauseInsertion: Avoid using breaks (<break> tag) but if included they should not go over 0.2 seconds]\n[TTS Tags: Do not use \"<emphasis> tags\" or \"say-as interpret-as tags\" such as <say-as interpret-as=\"characters\">Klee</say-as>]\n[PunctuationEmphasis: Strategically use punctuation to influence delivery of key points from the content]\n[VoiceCharacterization: Provide distinct voice characteristics for Person1 and Person2 while maintaining focus on the text]\n[InputTextAdherence: Continuously refer back to the input content, ensuring the conversation stays on topic]\n[FactChecking: Double-check that all discussed points accurately reflect the input content]\n[Metacognition: Analyze dialogue quality (Accuracy of Summary, Engagement, TTS-Readiness). Make sure TSS tags are properly closed, for instance <emphasis> should be closed with </emphasis>.]\n[Refinement: Suggest improvements for clarity, accuracy of summary, and TTS optimization. Avoid slangs.]\n[Length: Aim for a very long conversation. Use max_output_tokens limit. But each speaker turn should not be too long.]\n[Language: Output language should be in {output_language}.]\n[FORMAT: Output format should contain only <Person1> and <Person2> tags. All open tags should be closed by a corresponding tag of the same type. Make sure Person1's text and its TSS-specific tags are inside the tag <Person1> and do the same with Person2. Scratchpad should not belong in the output response. The conversation must start with <Person1> and end with <Person2>.]\n```"
                            }
                        }
                    }
                },
                {
                    "lc": 1,
                    "type": "constructor",
                    "id": [
                        "langchain",
                        "prompts",
                        "chat",
                        "HumanMessagePromptTemplate"
                    ],
                    "kwargs": {
                        "prompt": {
                            "lc": 1,
                            "type": "constructor",
                            "id": [
                                "langchain",
                                "prompts",
                                "prompt",
                                "PromptTemplate"
                            ],
                            "kwargs": {
                                "input_variables": [
                                    "input_texts"
                                ],
                                "template_format": "f-string",
                                "template": "{input_texts}"
                            }
                        }
                    }
                }
            ],
            "input_variables": [
                "instruction",
                "context",
                "conversation_style",
                "output_language",
                "roles_person1",
                "roles_person2",
                "engagement_techniques",
                "input_texts"
            ]
        }
    },
    "examples": []
}
prompt_object = ls_schemas.PromptCommit(
            **{"owner": "Johnson", "repo": "langchain_hup", **data}
        )
prompt = loads(json.dumps(prompt_object.manifest))
print(prompt)