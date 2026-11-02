from minidb import MiniDB

db = MiniDB("demo.log")
db.set("name", "Ada")
db.set("language", "Python")
print(db.get("name"))
db.delete("language")
print(db.keys())
