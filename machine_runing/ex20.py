import yaml

yaml_data = """

color_def:
  - &col1 "#ff0000"
  - &col2 "#00ff00"
  - &col3 "#0000ff"

color:
  title1: *col1
  title2: *col2
  title3: *col3

"""

data = yaml.load(yaml_data)

# 별칭을 이용한 출력
print(data)
print("title1 = ", data["color"]["title1"])
print("title2 = ", data["color"]["title2"])
print("title3 = ", data["color"]["title3"])