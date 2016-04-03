import anarapp.models
import inspect

for name, obj in inspect.getmembers(anarapp.models):
    if inspect.isclass(obj) and obj.__module__ == 'anarapp.models':
		if 'yacimiento' in obj.__dict__:
			print name
		
		#for field in obj._meta.fields:
		#	print '\t',field.name, ':', field.get_internal_type()
