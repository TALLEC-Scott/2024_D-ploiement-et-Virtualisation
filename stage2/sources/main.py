@app.post("/imgshape/")
async def imgshape(file: UploadFile):
    width = height = depth = 0
    bytes_as_np_array = np.frombuffer(await file.read(), dtype=np.uint8)
    try:
        img = cv2.imdecode(bytes_as_np_array, cv2.IMREAD_COLOR)
        if img is not None:
            height, width, depth = img.shape
    except Exception as e:
        return {"error": str(e)}

    return {"width": width, "height": height, "depth": depth}
