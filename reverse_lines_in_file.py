with open("dataset_24465_4.txt", "r") as f_in, open("output.txt", "w") as f_out:
    f_out.writelines(f_in.readlines()[::-1])