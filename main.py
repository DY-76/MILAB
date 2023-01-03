from sympy import im

import Modules.Collector as Collector
import Modules.Preprocessor as PPC
import Modules.Validator as Validator
import Modules.Calculator as Calculator

# # data Collect 지역코드 전국 = 00
# FileName = Collector.Colec(9999, 29, "Data/OriginalData")

# # ToSourceData
# PPC.ToSourceData("Data/OriginalData", "Data/SourceData", FileName)
#
# # ToValidatedData
# PPC.ToValidatedData("Data/OriginalData", "Data/SourceData", "20221111151618_p1")
#
# Validating Data
Validator.Validate("Data/OriginalData", "Data/SourceData", "Report", "20221111151618_p1")

# Calculating Data
Calculator.Calculate("Data/SourceData", "Data/SourceData", "D20221111151618_p1")
