#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2025/1/24 16:43
# @File  : t1.py.py
# @Author: johnson
# @Contact : github: johnson7788
# @Desc  :
from podcastfy.text_to_speech import TextToSpeech
from podcastfy.utils.config_conversation import load_conversation_config
import uuid
import os
import logging

logger = logging.getLogger(__name__)

def generate_audio(qa_content):
    conv_config = load_conversation_config()
    tts_config = conv_config.get("text_to_speech", {})
    output_directories = tts_config.get("output_directories", {})

    tts_model = "elevenlabs"
    api_key = "sk_22a0c1be5b03d7f4f4512ecfc37a5b9e3049fc24e67204d0"
    text_to_speech = TextToSpeech(
        model=tts_model,
        api_key=api_key,
        conversation_config=conv_config.to_dict(),
    )

    random_filename = f"podcast_{uuid.uuid4().hex}.mp3"
    audio_file = os.path.join(
        output_directories.get("audio", "data/audio"), random_filename
    )
    text_to_speech.convert_to_speech(qa_content, audio_file)
    print(f"Podcast generated successfully using {tts_model} TTS model, 声音文件是: {audio_file}")


if __name__ == '__main__':
    qa_content = '''"Welcome to PODCASTIFY - Your Personal Generative AI Podcast! Today, we're diving into the fascinating world of quantum computing. Are you ready to explore how it might revolutionize our future?"
 "Absolutely, I'm thrilled to join in! What's the essence of quantum computing, and how does it differ from our current computing systems?"
 "At its core, quantum computing is a physical device that follows the rules of quantum mechanics to perform high-speed mathematical and logical operations, storing and processing quantum information. Unlike classical computers that use bits to represent data as either 0 or 1, quantum computers use quantum bits, or qubits."
 "What makes qubits different from classical bits?"
 "Qubits can exist in a superposition of states, meaning they can be both 0 and 1 at the same time. This is thanks to quantum mechanics' principles of superposition and entanglement. Superposition allows a qubit to perform multiple calculations simultaneously, while entanglement means qubits can be interconnected, even at a distance."
 "That sounds incredible. But what are the practical implications of these principles?"
 "The potential is enormous. A quantum computer with just 50 qubits could outperform the world's most advanced supercomputers, and with 300 qubits, it could support more parallel computations than there are atoms in the universe. This could drastically reduce the time needed to solve complex problems in areas like cryptography, weather forecasting, and drug design."
 "It's fascinating to think about the impact on cryptography. Could quantum computing break traditional encryption methods?"
 "Yes, it could. However, it also offers new quantum secure encryption methods. The race is on to develop both quantum algorithms and traditional methods that can resist quantum attacks."
 "Let's talk about the challenges. Quantum computers are still in their infancy, right?"
 "Exactly. They're extremely fragile and prone to errors. But companies like Google are making significant progress. Google's latest chip, Willow, has shown promise in solving mathematical equations much faster than traditional computers."
 "And there's more to quantum computing than just solving complex problems. There's also the theoretical side, isn't there?"
 "Absolutely. The 1st CCF Quantum Computation Conference, for example, brought together experts to discuss the theoretical challenges and opportunities in quantum computing, including the limits of quantum algorithms, quantum error correction, and quantum circuit optimization."'''
    generate_audio(qa_content)