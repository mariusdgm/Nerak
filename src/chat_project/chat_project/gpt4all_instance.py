import os
from gpt4all import GPT4All

parent_dir = os.path.dirname(os.path.abspath(__file__))
for _ in range(3):
    parent_dir = os.path.dirname(parent_dir)
proj_root_dir = parent_dir

gptj = GPT4All("ggml-mpt-7b-chat", model_path=os.path.join(proj_root_dir, "gpt4all_models"))

chat_history = []