def snake to camel(word):
import re
return''.join(x.capitalize() or '_' for x in word.split('_'))
print(snake to camel(python))
