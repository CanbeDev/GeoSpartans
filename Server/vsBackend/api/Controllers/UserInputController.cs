using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using api.Data;
using Microsoft.AspNetCore.Mvc;
using api.models;

namespace api.Controllers
{
    [Route("api/[controller]")] // Fixed typo
    [ApiController]
    public class UserInputController : ControllerBase
    {
        private readonly ApplicationDBContext _context;

        public UserInputController(ApplicationDBContext context)
        {
            _context = context;
        }

        // GET: api/UserInput
        [HttpGet]
        public IActionResult GetAll()
        {
            var userInputs = _context.UserInputs.ToList();
            return Ok(userInputs);
        }

        // POST: api/UserInput
        [HttpPost]
        public async Task<ActionResult<UserInputModel>> CreateUserInput([FromBody] UserInputModel userInput)
        {
            if (userInput == null)
            {
                return BadRequest("Invalid user input data.");
            }

            // Add the new user input to the database
            _context.UserInputs.Add(userInput);
            await _context.SaveChangesAsync();

            // Return the created user input along with a 201 status code
            return CreatedAtAction(nameof(GetAll), new { id = userInput.Id }, userInput);
        }

        


    }
}
