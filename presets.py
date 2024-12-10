class EmptyLatentImagePresets:
    @classmethod
    def INPUT_TYPES(cls):  
        return {
        "required": {
             "dimensions": (
            [
                '512 x 512 (1:1)',
                '768 x 512 (1.5:1)',
                '896 x 512 (1.75:1)',
                '960 x 512 (1.875:1)',
                '1024 x 512 (2:1)',
                '1024 x 576 (1.778:1)',
                '1536 x 640 (2.4:1)',
                '1344 x 768 (1.75:1)',
                '1216 x 832 (1.46:1)',
                '1152 x 896 (1.286:1)',
                '1024 x 1024 (1:1)',
            ],
            {
            "default": '512 x 512 (1:1)'
             }),
           
            "invert": ("BOOLEAN", {"default": False}),
            "batch_size": ("INT", {
            "default": 1,
            "min": 1,
            "max": 4096
            }),
        },
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("Latent", "Width", "Height")
    FUNCTION = "generate"
    CATEGORY = "Simons Nodes"

    def generate(self, dimensions, invert, batch_size):
        from nodes import EmptyLatentImage
        result = [x.strip() for x in dimensions.split('x')]

        # Remove the aspect ratio part
        result[0] = result[0].split('(')[0].strip()
        result[1] = result[1].split('(')[0].strip()
        
        if invert:
            width = int(result[1].split(' ')[0])
            height = int(result[0])
        else:
            width = int(result[0])
            height = int(result[1].split(' ')[0])
        latent = EmptyLatentImage().generate(width, height, batch_size)[0]

        return (latent, int(width), int(height),)