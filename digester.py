import os
import httpx
import anthropic
import base64


def ask_claude_about_paper(
    pdf_path: str,
    message: str,
    model: str = "claude-3-5-sonnet-20241022",
) -> dict:
    """
    Send a message to Claude with a PDF attachment.
    Args:
        pdf_path (str): Path to the PDF file
        message (str): Message to send along with the PDF
        model (str): Model to use (defaults to Claude 3 Opus)
    Returns:
        dict: The API response
    """
    # get data
    pdf_data = base64.standard_b64encode(httpx.get(pdf_path).content).decode("utf-8")
    # Initialize the client
    client = anthropic.Anthropic()
    message = client.beta.messages.create(
        model=model,
        betas=["pdfs-2024-09-25"],
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_data,
                        },
                    },
                    {"type": "text", "text": message},
                ],
            }
        ],
    )

    text_content = ""
    for block in message.content:
        if block.type == "text":
            text_content += block.text

    return text_content
