using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using api.models;
using Microsoft.EntityFrameworkCore;

namespace api.Data
{
    public class ApplicationDBContext : DbContext
    {
        public ApplicationDBContext(DbContextOptions<ApplicationDBContext> options) : base(options)
        {
        }

        public DbSet<UserInputModel> UserInputs { get; set; }
        public DbSet<PredictionResultModel> PredictionResults { get; set; }

        //protected override void OnModelCreating(ModelBuilder modelBuilder)
        //{
            //modelBuilder.Entity<UserInputModel>().HasKey(u => u.Id); // Ensure Id is the primary key
            //modelBuilder.Entity<PredictionResultModel>().HasKey(p => p.Id); // Ensure Id is the primary key

            // Configure any other relationships or constraints as needed
        //}

         protected override void OnModelCreating(ModelBuilder modelBuilder)
 {
     modelBuilder.Entity<UserInputModel>(entity =>
     {
            entity.HasKey(e => e.Id);
            
            entity.Property(e => e.Id).HasColumnName("USER_ID");
            entity.Property(e => e.CropType ).IsRequired();
            entity.Property(e => e.FarmSize ).IsRequired();
            entity.Property(e => e.Area).IsRequired();
            entity.Property(e => e.Season).IsRequired();
                        
     });

     modelBuilder.Entity<PredictionResultModel>(entity =>
     {
         entity.HasKey(e => e.Id);
         
     });
 }
    }
}