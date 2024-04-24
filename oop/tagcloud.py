class TagCloud:
    def __init__(self):
        # private attribute
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        # return self.tags[tag.lower()]
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud)
cloud.add("python")
cloud.add("js")
print(cloud["python"])
cloud["python"] = 10
print(cloud["python"])
print(len(cloud))

for tag in cloud:
    print(tag)
print("-" * 15)
# print(cloud.__tags)
print(cloud["PYTHON"])
print(cloud["pythoN"])
# print(cloud.__tags["python"])
# print(cloud.__tags["PYTHON"])
print(cloud.__dict__)
print(cloud._TagCloud__tags)
