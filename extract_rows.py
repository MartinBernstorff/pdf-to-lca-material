import json
from collections import defaultdict
from typing import Literal, Sequence

import instructor
from joblib import Memory
from openai import OpenAI
from openai.types.chat.chat_completion_user_message_param import (
    ChatCompletionUserMessageParam,
)

mem = Memory(location="./cache", verbose=0)

OPENAI_MODELS = Literal["gpt-4-turbo-preview", "gpt-4-1106-preview", "gpt-3.5-turbo"]


def json_to_dict(json_input: str) -> dict[str, Sequence[str]]:
    rows = json.loads(json_input)

    dataframe_rows = defaultdict(list)
    for row in rows:
        for key, value in row.items():
            dataframe_rows[key].append(value)

    return dataframe_rows


@mem.cache
def get_completion(
    api_key: str,
    model: OPENAI_MODELS,
    prompt: str,
    cache_version: int,
):
    client = instructor.patch(OpenAI(api_key=api_key))
    completion = client.chat.completions.create(  # type: ignore
        model=model,
        messages=[
            ChatCompletionUserMessageParam(role="user", name="UserName", content=prompt)
        ],
        temperature=0.0,
    )
    return completion.choices[0].message.content
