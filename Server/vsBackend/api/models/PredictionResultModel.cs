using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace api.models
{
    public class PredictionResultModel
    {
    [Key]
    public int Id { get; set; }


    //public DateTime PredictionDate { get; set; }

    public double PredictionValue { get; set; }

    public string ModelUsed { get; set; } = string.Empty;

    //public string InputData { get; set; } = string.Empty;

    //public double ConfidenceScore { get; set; }

    //public string Status { get; set; } = string.Empty;

    //public DateTime CreatedDate { get; set; }

    //public DateTime? UpdatedDate { get; set; }

    public int? UserId { get; set; }

    public string Context { get; set; } = string.Empty;

    // Property to store the binary data (e.g., pickle file)
    //public byte[]? PickleData { get; set; } 
    }
}