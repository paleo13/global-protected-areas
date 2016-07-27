### Initialization
# load libraries
import arcpy
import toml

### Preliminary processing
# load parameters
with open("general.toml") as conffile:
	general_params = toml.loads(conffile.read())
with open("rasterize.toml") as conffile:
	rasterize_params = toml.loads(conffile.read())

# set environmental variables
arcpy.env.parallelProcessingFactor=general_params['threads']

### Main processing
# rasterize data
arcpy.FeatureToRaster_conversion(
	'data/intermediate/06/WDPA-shapefile-dissolved.shp', 'data/intermediate/07/WDPA.tif',
	cell_size=rasterize_params['cell_size'],
)




 
