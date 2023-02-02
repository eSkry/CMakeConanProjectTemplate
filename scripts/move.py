import os
import shutil


class Move:
    def __init__(self, base_build_dir, base_destination_dir, append_files=[]):
        self.base_build_dir = base_build_dir
        self.base_destination_dir = base_destination_dir

        # src = base_build_dir
        # dst = base_destination_dir
        # (src, dst)
        self.copy_files = [
            ("bin/MyProject-1.0.0", "."),
            ("bin/MyProject", ".")
        ]

        if append_files:
            self.copy_files.extend(append_files)

    def copy(self):
        # Кеш созданных директорий. Нужен чтобы уменьшить количество проверок exists.
        cdir_cache = []

        if not os.path.exists(self.base_destination_dir):
            os.makedirs(self.base_destination_dir)
            cdir_cache.append(self.base_destination_dir)

        for file in self.copy_files:
            src = os.path.join(self.base_build_dir, file[0])
            dst = os.path.join(self.base_destination_dir, file[1])

            if os.path.isfile(src):
                print(f"Copy file: '{src}' => '{dst}'")
                shutil.copy2(src, dst)
            elif os.path.isdir(src):
                print(f"Copy dir: '{src}' => '{dst}'")
                shutil.copytree(src, dst)

