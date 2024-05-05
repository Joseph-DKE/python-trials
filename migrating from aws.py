import cs50, requests, shutil


db = cs50.SQL("postgresql://postgres.mmonniwlygphymfpeqah:^oxvERwGyTHbJM7@aws-0-us-east-1.pooler.supabase.com:5432/postgres")

ss = db.execute("SELECT * from aspirants")

def get_files(file_name):
    url = f"https://dlluikxkn9df3.cloudfront.net/{file_name}"

    return url

for s in ss:
    try:
        name = s["picture"]
        url = get_files(f'darkstech/{name}')
        print(url)
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Open a new file in binary write mode
            with open(s["picture"], 'wb') as file:
                # Copy the image content to the file
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
            print("Image downloaded successfully as", ss[0]["picture"])
        else:
            print("Failed to download image")
    except:
        print("No Pic")