
UPLOAD_FOLDER = "uploads"
DOWNLOAD_FOLDER = "downloads"



i =0 
# while loop
while i > -1

    function convertfile()

        res = readdir(UPLOAD_FOLDER)

        for file in res

            convertCommand = "pyinstaller --onefile " * UPLOAD_FOLDER * "/" * file

            bin = "pyinstaller"

            type_bin = "--onefile"

            type_file = UPLOAD_FOLDER * "/" * file

            print(convertCommand)

            run(`$bin $type_bin $type_file`)

            exe = replace(file, ".py" => ".exe")

            full_path = "dist/" * exe

            destination = "downloads"

            mv(full_path, joinpath(destination, basename(full_path)))
            
            rm(UPLOAD_FOLDER*"/"*file)

            rm("build", recursive=true)
            dir = "./"
            foreach(rm, filter(endswith(".spec"), readdir(dir,join=true)))


        end
    
        


    end # Function end
    
    # Function call
    convertfile()
  

      

end # Ending Loop

