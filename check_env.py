import sys, site, platform

print ("Python:", sys.executable)
print ("Version:", platform.python_version())
print ("API version:", sys.api_version)
print ("base prefix:", sys.base_prefix)
print ("base exec prefix:", sys.base_exec_prefix)
print ("path:", sys.path)
print ("platform:", sys.platform)
print ("version_info:", sys.version_info)
print ("platlibdir:", sys.platlibdir)
print ("Branch:", platform.python_branch())
print ("Build:", platform.python_build())
print ("Implementation:", platform.python_implementation())
print ("Revision:", platform.python_revision())
print ("Compiler:", platform.python_compiler())
print ("Version Tuple:", platform.python_version_tuple())
print ("Site-packages:", site.getsitepackages())
print ("User site-packages:", site.getusersitepackages())
print ("Userbase:", site.getuserbase())



