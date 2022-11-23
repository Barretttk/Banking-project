using System.Diagnostics;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using EPBanking.Models;

namespace EPBanking.Controllers;

public class UserController : Controller
{
    private MyContext DATABASE;

    public UserController(MyContext context)
    {
        DATABASE = context;
    }


    [HttpGet]
    [Route("")]
    public IActionResult Index()
    {
        return View("Index");
    }

    [HttpPost]
    [Route("/register")]
    public IActionResult Register(User newUser)
    {
        if (ModelState.IsValid)
        {
            if (DATABASE.Users.Any(user => user.Email == newUser.Email))
            {
                ModelState.AddModelError("Email", "is taken");
            }
        }

        if (ModelState.IsValid == false)
        {
            return Index();
        }

        PasswordHasher<User> hashBrowns = new PasswordHasher<User>();
        newUser.Password = hashBrowns.HashPassword(newUser, newUser.Password);

        DATABASE.Users.Add(newUser);
        DATABASE.SaveChanges();

        HttpContext.Session.SetInt32("UUID", newUser.UserId);
        HttpContext.Session.SetString("Name", newUser.FullName());
        return RedirectToAction("Discover", "Project");

    }

    [HttpPost]
    [Route("/login")]
    public IActionResult Login(LoginUser loginUser)
    {
        if (ModelState.IsValid == false)
        {
            return Index();
        }

        User? dbUser = DATABASE.Users.FirstOrDefault(user => user.Email == loginUser.LoginEmail);

        if (dbUser == null)
        {
            ModelState.AddModelError("LoginEmail", "not found");
            return Index();
        }

        PasswordHasher<LoginUser> hashBrowns = new PasswordHasher<LoginUser>();
        PasswordVerificationResult pwCompareResult = hashBrowns.VerifyHashedPassword(loginUser, dbUser.Password, loginUser.LoginPassword);

        if (pwCompareResult == 0)
        {
            ModelState.AddModelError("LoginPassword", "is not correct");
            return Index();
        }

        HttpContext.Session.SetInt32("UUID", dbUser.UserId);
        HttpContext.Session.SetString("Name", dbUser.FullName());
        return RedirectToAction("Discover", "Project");
    }

    [HttpPost]
    [Route("/logout")]
    public IActionResult Logout()
    {
        HttpContext.Session.Clear();
        return RedirectToAction("Index");
    }
}