from typing import Optional


class GenerateImageTitle:
    @staticmethod
    def INPUT_TYPES():
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
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

    def generate_title(self, prompt: str, resolution:Optional[int]=None, scale_factor:Optional[float]=None):
        # Process prompt
        descriptive_title = " ".join(
            word.capitalize() for word in prompt.split() if len(word) > 2
        )

        # Append resolution and scale factor if provided
        if resolution:
            descriptive_title += f" - {resolution}px"
        if scale_factor:
            descriptive_title += f" x{scale_factor}"

        # Return the final title
        return (descriptive_title,)


# Register the custom node
NODE_CLASS_MAPPINGS = {"Generate Image Title": GenerateImageTitle}