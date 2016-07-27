### Initialization
# load libraries
import arcpy
import toml
import sys

### Preliminary processing
# load parameters
with open("general.toml") as conffile:
	general_params = toml.loads(conffile.read())

# set environmental variables
arcpy.env.parallelProcessingFactor=general_params['threads']

### Main processing
# calculate radius
arcpy.AddField_management(sys.argv[1], 'REP_RADIUS', 'DOUBLE')
arcpy.CalculateField_management(sys.argv[1], 'REP_RADIUS', 'math.sqrt(!REP_AREA!/math.pi())')

# buffer points to polygon
arcpy.Buffer_analysis(sys.argv[1], sys.argv[2], 'REP_RADIUS')
