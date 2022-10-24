import Modules.Collector as Collector
import Modules.Preprocessor as PPC
import Modules.Validator as Validator

# data Collect
FileName = Collector.Colec(9999, 29, "Data/OriginalData")

# ToSourceData
PPC.ToSourceData("Data/OriginalData", "Data/SourceData", FileName)

# ToValidatedData
PPC.ToValidatedData("Data/SourceData", "Data/ValidatedData", "SD_"+FileName)

# Validating Data
Validator.Validate("Data/ValidatedData", "Data/ValidatedData", "Report", "VD_SD_"+FileName)