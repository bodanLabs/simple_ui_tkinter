def write(file_path,data):
    try:
        with open(file_path,'a') as fw:
            fw.write(data)
    except FileNotFoundError as e:
        print(f"The file couldn't be open -> {e}")
    except Exception as e:
        print(e)