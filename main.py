import marimo

__generated_with = "0.4.7"
app = marimo.App(width="full")


@app.cell
def __():
    import marimo as mo

    return (mo,)


@app.cell
def __(mo):
    mo.md(
        rf"""To get started, enter your OpenAI API key.

    You can generate one [here](https://platform.openai.com/api-keys)."""
    )
    return


@app.cell
def __(mo):
    api_key = mo.ui.text(
        label="OpenAI API key", kind="password", placeholder="Insert here"
    )
    api_key
    return (api_key,)


@app.cell
def __(mo):
    mo.md(rf"Then, upload the file you would like to process.")
    return


@app.cell
def __(mo):
    file = mo.ui.file(kind="area")
    file
    return (file,)


@app.cell
def __(file):
    from pdf_to_text import pdf_to_text
    from io import BytesIO

    # Get the first page
    text_content = pdf_to_text(BytesIO(file.contents()))
    return BytesIO, pdf_to_text, text_content


@app.cell
def __(mo):
    mo.md(
        "Lastly, trim the file to only contain the table(s) you would like to extract."
    )
    return


@app.cell
def __(mo, text_content):
    interval = mo.ui.range_slider(
        label="Which part of the contents to keep. See a preview below.",
        start=0,
        stop=len(text_content),
        full_width=True,
    )
    interval
    return (interval,)


@app.cell
def __(interval, text_content):
    trimmed_text_content = text_content[interval.value[0] : interval.value[1]]
    trimmed_text_content
    return (trimmed_text_content,)


@app.cell
def __(api_key, trimmed_text_content):
    from rows_from_str import get_completion

    rows = get_completion(
        api_key=api_key.value,
        model="gpt-3.5-turbo",
        prompt=f"The following is one or more tables from a pdf.  <tables>{trimmed_text_content}</tables> Extract the rows as valid JSON. The first value is typically a label, so add a 'label' key. Be sure to extract all rows, and to preserve the cell values verbatim.",
        cache_version=3,
    )
    return get_completion, rows


@app.cell
def __(rows):
    from rows_from_str import json_to_dict

    df_rows = json_to_dict(rows)
    return df_rows, json_to_dict


@app.cell
def __(df_rows, mo):
    import polars as pl

    mo.ui.table(pl.DataFrame(df_rows))
    return (pl,)


if __name__ == "__main__":
    app.run()
