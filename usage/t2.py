#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2025/1/24 20:29
# @File  : t2.py
# @Author: johnson
# @Contact : github: johnson7788
# @Desc  :

# set the LANGSMITH_API_KEY environment variable (create key in settings)
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
prompt = hub.pull("souzatharsis/podcastfy_longform")
print(prompt)


