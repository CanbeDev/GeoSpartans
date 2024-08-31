using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace api.models
{
    public class UserInputModel
    {
        [Key]
        public int Id { get; set; }

        public string CropType { get; set; } = string.Empty;

        public string FarmSize { get; set; } = string.Empty;

        public string Area { get; set; } = string.Empty;

        public string Season { get; set; } = string.Empty;

        public int MyProperty { get; set; } // Assuming MyProperty is an integer type
    }
}