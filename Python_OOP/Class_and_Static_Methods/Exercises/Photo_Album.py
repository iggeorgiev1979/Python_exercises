from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.free_page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        if len(self.photos[self.free_page]) == 4:
            self.free_page += 1
        if self.free_page < self.pages:
            self.photos[self.free_page].append(label)
            return f"{label} photo added successfully on page {self.free_page + 1} slot {len(self.photos[self.free_page])}"
        return "No more free slots"

    def display(self):
        return "\n".join(self.generate_album())

    def generate_album(self):
        result = ["-----------"]
        for page in self.photos:
            tmp = ["[]"] * len(page)
            result.append(" ".join(tmp))
            result.append("-----------")
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
