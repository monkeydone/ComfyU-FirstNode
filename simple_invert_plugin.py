class SimpleInvert:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "invert_image"
    CATEGORY = "Image Processing"

    def invert_image(self, image):
        # 将图像的像素值取反
        inverted_image = 1.0 - image
        return (inverted_image,)


# 导出节点映射
NODE_CLASS_MAPPINGS = {
    "SimpleInvert": SimpleInvert
}

# 导出节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleInvert": "Simple Invert Node"
}
