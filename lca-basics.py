import marimo

__generated_with = "0.4.7"
app = marimo.App()


@app.cell
def __():
    import selenium
    return selenium,


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    file = mo.ui.file(kind="area")
    file
    return file,


@app.cell
def __(file):
    type(file.contents())
    return


@app.cell
def __(file):
    import PyPDF2
    from io import BytesIO

    # assume 'pdf_bytes' is a bytes object containing the PDF file

    # Create a BytesIO object from the bytes
    pdf_stream = BytesIO(file.contents())

    # Create a PyPDF2 reader object
    pdf = PyPDF2.PdfReader(pdf_stream)

    # Get the first page
    content = ("––– NEXT PAGE –––").join(page.extract_text() for page in pdf.pages)
    content
    return BytesIO, PyPDF2, content, pdf, pdf_stream


@app.cell
def __(ChatCompletionUserMessageParam):
    import instructor
    from dataclasses import dataclass
    from openai import AsyncOpenAI

    from typing import Literal

    OPENAI_MODELS = Literal[
        "gpt-4-turbo-preview", "gpt-4-1106-preview", "gpt-3.5-turbo"
    ]


    @dataclass
    class OpenAICompleter:
        api_key: str
        model: OPENAI_MODELS

        def __post_init__(self):
            self.client = instructor.patch(AsyncOpenAI(api_key=self.api_key))
            self.completer = self.client.chat.completions

        async def __call__(self, prompt: str) -> str:
            completion = await self.completer.create(
                model=self.model,
                messages=[
                    ChatCompletionUserMessageParam(
                        role="user", name="UserName", content=prompt
                    )
                ],
                temperature=0.0,
            )
            completion_str = completion.choices[0].message.content

            if not completion_str:
                raise ValueError(f"Completion was not a string: {completion_str}")

            return completion_str
    return (
        AsyncOpenAI,
        Literal,
        OPENAI_MODELS,
        OpenAICompleter,
        dataclass,
        instructor,
    )


app._unparsable_cell(
    r"""
    completer = OpenAICompleter(api_key=)
    """,
    name="__"
)


if __name__ == "__main__":
    app.run()
