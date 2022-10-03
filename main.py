import Modules.Collector as Collector
import Modules.Preprocessor as PPC
import Modules.Validator as Validator

# # data Collect
# FileName = Collector.Colec(9999, 29, "Data/OriginalData")

# # ToSourceData
# PPC.ToSourceData("Data/OriginalData", "Data/SourceData", FileName)
#
# # ToValidatedData
# PPC.ToValidatedData("Data/SourceData", "Data/ValidatedData", "SD_"+FileName)

Validator.Validate("Data/OriginalData", "Data/ValidatedData", "Report", "20221003124745")