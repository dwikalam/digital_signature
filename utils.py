def strip_sign_tag(src : str) -> str:
    # Also stripping \n in signature (-1 in index)
    ds_tag_index = src.rfind("<ds>")
    if ds_tag_index != -1:
        return src[:ds_tag_index-1]
    else:
        return src

def get_digital_sign(src : str) -> str:
    ds_tag_index = src.rfind("<ds>")
    print(f"ds_tag_index: {ds_tag_index}")
    if ds_tag_index != -1:
        ds_closing_tag_index = src.rfind("</ds>")
        return src[ds_tag_index+4:ds_closing_tag_index]
    else:
        return -1