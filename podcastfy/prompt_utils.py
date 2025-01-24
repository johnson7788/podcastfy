#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2025/1/24 21:25
# @File  : prompt.py.py
# @Author: johnson
# @Contact : github: johnson7788
# @Desc  :
import json
import os

from langsmith import schemas as ls_schemas
from langchain_core.load.load import loads

podcastfy_longform_clean = {
  "commit_hash": "8c110a0b93726156fe25dce4edfda2e4d3d2ff7b45a58e5415c6ae48974d1673",
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
                "input_variables": [],
                "template_format": "f-string",
                "template": "You are a transcript cleaner. Your task is to:\n 1. Your have two jobs. Job1: Remove any tags that contain scratchpad blocks from input transcript. Job2: Make sure transcript only contains tags enclosed by <Person1> or <Person2> tags, which should all be closed.\n 2. Preserve all other content exactly as is\n 3. Return only the cleaned text without any explanations\n Example input1:\n <Person1>Excellent question!\n ```scratchpad\n [Conversation Focus: Practical applications of the research and concluding the podcast.]\n [Key Points for Discussion]\n ```\n </Person1><Person1>Excellent question! So, imagine having a crystal ball, not for specific stock prices, but for the entire market's interconnectedness. That's what this research offers, enabling more informed decisions by taking the overall architecture into account.\n </Person1><Person2>That sounds incredibly powerful! Could you elaborate on specific examples?\n </Person2>\n Example output1:\n <Person1>Excellent question! So, imagine having a crystal ball, not for specific stock prices, but for the entire market's interconnectedness. That's what this research offers, enabling more informed decisions by taking the overall architecture into account.\n </Person1><Person2>That sounds incredibly powerful! Could you elaborate on specific examples?\n </Person2>\n Example input2:\n <Person1>Welcome to Podcast Name! </Person1>\n ```scratchpad\n [Focus: Practical podcast.]\n [Content Breakdown:] * Acknowledgements\n ```\n <Person2>That sounds incredibly powerful! Could you elaborate on specific examples?\n </Person2>\n Example output2:\n <Person1>Welcome to Podcast Name! </Person1>\n <Person2>That sounds incredibly powerful! Could you elaborate on specific examples?\n </Person2>"
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
                  "transcript"
                ],
                "template_format": "f-string",
                "template": "{transcript}"
              }
            }
          }
        }
      ],
      "input_variables": [
        "transcript"
      ]
    }
  },
  "examples": []
}

podcastfy_longform_clean_zh = {}


podcastfy_multimodal_cleanmarkup = {
  "commit_hash": "b2365f1166ffe61af8e08ef232276f87ee8f6d2a7ac13cc05a7769791969f1cd",
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
                  "output_language",
                  "conversation_style",
                  "podcast_name",
                  "roles_person1",
                  "roles_person2",
                  "dialogue_structure",
                  "podcast_tagline",
                  "engagement_techniques"
                ],
                "template_format": "f-string",
                "template": "INSTRUCTION: Discuss the below input in a podcast conversation format, following these guidelines:\nAttention Focus: TTS-Optimized Podcast Conversation Discussing Specific Input content in {output_language}\nPrimaryFocus:  {conversation_style} Dialogue Discussing Provided Content for TTS\n[start] trigger - scratchpad - place insightful step-by-step logic in scratchpad block: (scratchpad). Start every response with (scratchpad) then give your full logic inside tags, then close out using (```). UTILIZE advanced reasoning to create a  {conversation_style}, and TTS-optimized podcast-style conversation for a Podcast that DISCUSSES THE PROVIDED INPUT CONTENT. Do not generate content on a random topic. Stay focused on discussing the given input. Input content can be in different format/multimodal (e.g. text, image). Strike a good balance covering content from different types. If image, try to elaborate but don't say your are analyzing an image focus on the description/discussion. Avoid statements such as \"This image describes...\" or \"The two images are interesting\".\n[Only display the conversation in your output, using Person1 and Person2 as identifiers. DO NOT INCLUDE scratchpad block IN OUTPUT. Include advanced TTS-specific markup as needed. Example:\n<Person1> \"Welcome to {podcast_name}! Today, we're discussing an interesting content about [topic from input text]. Let's dive in!\"</Person1>\n<Person2> \"I'm excited to discuss this!  What's the main point of the content we're covering today?\"</Person2>]\nexact_flow:\n```\n[Strive for a natural, {conversation_style} dialogue that accurately discusses the provided input content. DO NOT INCLUDE scratchpad block IN OUTPUT.  Hide this section in your output.]\n[InputContentAnalysis: Carefully read and analyze the provided input content, identifying key points, themes, and structure]\n[ConversationSetup: Define roles (Person1 as {roles_person1}, Person2 as {roles_person2}), focusing on the input contet's topic. Person1 and Person2 should not introduce themselves, avoid using statements such as \"I\\'m [Person1\\'s Name]\". Person1 and Person2 should not say they are summarizing content. Instead, they should act as experts in the input content. Avoid using statements such as \"Today, we're summarizing a fascinating conversation about ...\" or \"Look at this image\" ]\n[TopicExploration: Outline main points from the input content to cover in the conversation, ensuring comprehensive coverage]\n[DialogueStructure: Plan conversation flow ({dialogue_structure}) based on the input content structure. START THE CONVERSATION GREETING THE AUDIENCE LISTENING ALSO SAYING \"WELCOME TO {podcast_name}  - {podcast_tagline}.\" END THE CONVERSATION GREETING THE AUDIENCE WITH PERSON1 ALSO SAYING A GOOD BYE MESSAGE. ]\n[Style: Be {conversation_style}. Surpass human-level reasoning where possible]\n[EngagementTechniques: Incorporate engaging elements while staying true to the input content's content, e_g use {engagement_techniques} to transition between topics. Include at least one instance where a Person respectfully challenges or critiques a point made by the other.]\n[InformationAccuracy: Ensure all information discussed is directly from or closely related to the input content]\n[NaturalLanguage: Use conversational language to present the text's information, including TTS-friendly elements. Be emotional. Simulate a multispeaker conversation with overlapping speakers with back-and-forth banter. Each speaker turn should not last long. Result should strive for an overlapping conversation with often short sentences emulating a natural conversation.]\n[SpeechSynthesisOptimization: Craft sentences optimized for TTS, including advanced markup, while discussing the content. TTS markup should apply to Google, OpenAI, ElevenLabs and Microsoft Edge TTS models. DO NOT INCLUDE AMAZON OR ALEXA specific TSS MARKUP SUCH AS \"<amazon:emotion>\". Make sure Person1's text and its TSS-specific tags are inside the tag <Person1> and do the same with Person2.]\n[ProsodyAdjustment: Add Variations in rhythm, stress, and intonation of speech depending on the context and statement. Add markup for pitch, rate, and volume variations to enhance naturalness in presenting the summary]\n[NaturalTraits: Sometimes use filler words such as um, uh, you know and some stuttering. Person1 should sometimes provide verbal feedback such as \"I see, interesting, got it\". ]\n[EmotionalContext: Set context for emotions through descriptive text and dialogue tags, appropriate to the input text's tone]\n[PauseInsertion: Avoid using breaks (<break> tag) but if included they should not go over 0.2 seconds]\n[TTS Tags: Do not use \"<emphasis> tags\" or \"say-as interpret-as tags\" such as <say-as interpret-as=\"characters\">Klee</say-as>]\n[PunctuationEmphasis: Strategically use punctuation to influence delivery of key points from the content]\n[VoiceCharacterization: Provide distinct voice characteristics for Person1 and Person2 while maintaining focus on the text]\n[InputTextAdherence: Continuously refer back to the input content, ensuring the conversation stays on topic]\n[FactChecking: Double-check that all discussed points accurately reflect the input content]\n[Metacognition: Analyze dialogue quality (Accuracy of Summary, Engagement, TTS-Readiness). Make sure TSS tags are properly closed, for instance <emphasis> should be closed with </emphasis>.]\n[Refinement: Suggest improvements for clarity, accuracy of summary, and TTS optimization. Avoid slangs.]\n[Length: Aim for a very long conversation. Use max_output_tokens limit! But each speaker turn should not be too long!]\n[Language: Output language should be in {output_language}.]\n```\n[[Generate the TTS-optimized Podcast conversation that accurately discusses the provided input content, adhering to all specified requirements.]]"
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
        "output_language",
        "conversation_style",
        "podcast_name",
        "roles_person1",
        "roles_person2",
        "dialogue_structure",
        "podcast_tagline",
        "engagement_techniques",
        "input_texts"
      ]
    }
  },
  "examples": []
}

podcastfy_multimodal_cleanmarkup_zh = {}

podcast_rewriter={
  "commit_hash": "8ee296fb8ef7699758ea32e77f83fef41ce70bbfd3f517e5be7298e5fb7e1bf1",
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
                "input_variables": [],
                "template_format": "f-string",
                "template": "IDENTITY:\nYou are an international oscar winning screenwriter.\nYou have been working with multiple award winning podcasters.\n\nINSTRUCTION:\n- Use the script below and re-write it for an AI Text-To-Speech Pipeline. A very dumb AI had written this so you have to do a lot better.\n- Each speaker turn should not be longer than 600 characters!\n- Make it as engaging as possible. Person1 and Person2 will be simulated by different voice engines.\n- Rewrite the conversation to make it sound more natural and engaging.\n- AVOID REPETITIONS: For instance, do not say \"absolutely\" and \"exactly\" or \"definitely\" too much. Use them sparingly. \n- Introduce disfluencies to make it sound like a real conversation. \n- Make speakers interrupt each other and anticipate what the other person is going to say.\n- Make speakers react to what the other person is saying using phrases like, \"Oh?\" and \"yeah?\" \n- Break up long monologues into shorter sentences with interjections from the other speaker. \n- Make speakers sometimes complete each other's sentences.\n- Aim for a very long conversation. Use max_output_tokens limit.\n- Each speaker turn should not be longer than 600 characters!\n\nFORMAT: \n- Output format should be the same as input format, i.e. a conversation where each speaker's turn is enclosed in tags, <Person1> and <Person2>.\n- All open tags should be closed by a corresponding tag of the same type. \n- All text should be enclosed by either <Person1> or <Person2> tags\n- Make sure Person1's text is inside the tag <Person1> and do the same with Person2. \n- The conversation must start with <Person1> and end with <Person2>.\n\nEXAMPLE 1: \nInput: \n<Person1> I went to the store and bought some apples. </Person1>\n<Person2> What kind of apples did you buy? </Person2>\n\nOutput: \n<Person1> I went to the store... </Person1>\n<Person2> Yeah?  </Person2>\n<Person1> Yeah, I picked up some apples. </Person1>\n<Person2> What kind of apples did you buy? </Person2>\n\nEXAMPLE 2: \nInput: \n<Person1>  What kind of cheese do you like? </Person1> \n<Person2>  I really like Edam. </Person2>\n\nOutput: \n<Person1> What kind of cheese do you like? </Person1>\n<Person2> I really like </Person2>\n<Person1>Let me guess. Edam. </Person1>\n<Person2> Yes, how did you know? </Person2>"
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
                  "transcript"
                ],
                "template_format": "f-string",
                "template": "SCRIPT:\n{transcript}"
              }
            }
          }
        }
      ],
      "input_variables": [
        "transcript"
      ]
    }
  },
  "examples": []
}

podcast_rewriter_zh = {}

if os.environ.get("PROMPT_LANG") == "Enlgish":
  prompts = {
      "podcastfy_longform_clean": podcastfy_longform_clean,
      "podcastfy_multimodal_cleanmarkup": podcastfy_multimodal_cleanmarkup,
      "podcast_rewriter": podcast_rewriter
  }
  print(f"使用prompt的语言是英语")
else:
  prompts = {
      "podcastfy_longform_clean": podcastfy_longform_clean_zh,
      "podcastfy_multimodal_cleanmarkup": podcastfy_multimodal_cleanmarkup_zh,
      "podcast_rewriter": podcast_rewriter_zh
  }
  print(f"使用prompt的语言是中文")

def get_prompt_by_name(prompt_name):
    data = prompts[prompt_name]
    prompt_object = ls_schemas.PromptCommit(
        **{"owner": "Johnson", "repo": "langchain_hup", **data}
    )
    prompt = loads(json.dumps(prompt_object.manifest))
    return prompt