#program of setcomprehension
friends=['Suman','Kalia','Rinku']
guests=['Somi','Kajal','Suman','Kalia']
friends_lower={i.lower() for i in friends}
guests_lower={j.lower() for j in guests}
print(friends_lower)
print(guests_lower)
friend_common={name.title() for name in friends_lower.intersection(guests_lower)}
print(friend_common)
student=['suman','deva','kalia']
age=[23,56,78]
student_info={ student[i]:age[i] for i in range(len(student)) if age[i]>10}
print(student_info)
