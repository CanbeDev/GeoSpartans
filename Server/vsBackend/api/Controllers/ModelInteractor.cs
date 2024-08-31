using System.Diagnostics;

namespace api.Controllers
{
    public class ModelInteractor
    {
        public string RunPythonScript(string input)
        {
            var start = new ProcessStartInfo
            {
                FileName = "python",
                Arguments = $"your_script.py \"{input}\"",
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            using (var process = Process.Start(start))
            using (var reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                return result;
            }
        }
    }
}
