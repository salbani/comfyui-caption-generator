from typing import Optional
import openai  # Ensure you have the OpenAI Python SDK installed


class GenerateImageTitle:
    DEPENDENCIES = {
        "required": ["openai"],  # Automatically installs via pip
    }

    @staticmethod
    def INPUT_TYPES():
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "openai_api_key": ("STRING", {"multiline": False}),  # API key widget
            },
            "optional": {
                "width": ("INT", {"default": None}),
                "height": ("INT", {"default": None}),
                "scale_factor": ("FLOAT", {"default": None}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_title"

    CATEGORY = "Utility"

    def generate_title(
        self,
        prompt: str,
        openai_api_key: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        scale_factor: Optional[float] = None,
    ):
        openai.api_key = openai_api_key.strip()
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Condense tag-style prompts into descriptive titles.",
                    },
                    {
                        "role": "user",
                        "content": f"Condense this prompt into a title: {prompt}",
                    },
                ],
                max_tokens=30,
            )
            title = response.choices[0].message.content.strip()  # type: ignore
            if width is not None:
                title = f"{title}_{width}x"
                if height is not None:
                    title = f"{title}{height}"
                if scale_factor is not None:
                    title = f"{title}@{scale_factor}x"
        except Exception as e:
            title = f"Error generating title: {str(e)}"

        return (title,)


# Register the custom node
NODE_CLASS_MAPPINGS = {"Generate Image Title": GenerateImageTitle}
