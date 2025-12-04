const { test, expect } = require("@playwright/test");

function uniqueEmail(prefix = "user") {
  return `${prefix}_${Date.now()}@example.com`;
}

// Positive: register with valid data
test("registers user with valid data", async ({ page }) => {
  const email = uniqueEmail("reg");

  await page.goto("/static/register.html");
  await page.fill("#email", email);
  await page.fill("#password", "password123");
  await page.fill("#confirm", "password123");
  await page.click("button[type='submit']");

  await expect(page.locator("#message")).toContainText("Registration successful");
});

// Positive: login with correct credentials
test("logs in with correct credentials", async ({ page }) => {
  const email = uniqueEmail("login");

  // register first
  await page.goto("/static/register.html");
  await page.fill("#email", email);
  await page.fill("#password", "password123");
  await page.fill("#confirm", "password123");
  await page.click("button[type='submit']");
  await expect(page.locator("#message")).toContainText("Registration successful");

  // now login
  await page.goto("/static/login.html");
  await page.fill("#email", email);
  await page.fill("#password", "password123");
  await page.click("button[type='submit']");

  await expect(page.locator("#message")).toContainText("Login successful");
});

// Negative: short password on register
test("shows error for short password on register", async ({ page }) => {
  const email = uniqueEmail("short");

  await page.goto("/static/register.html");
  await page.fill("#email", email);
  await page.fill("#password", "123");
  await page.fill("#confirm", "123");
  await page.click("button[type='submit']");

  await expect(page.locator("#message")).toContainText("Password must be at least 8 characters.");
});

// Negative: wrong password on login
test("shows error for wrong login password", async ({ page }) => {
  const email = uniqueEmail("wrongpw");

  // correct registration
  await page.goto("/static/register.html");
  await page.fill("#email", email);
  await page.fill("#password", "password123");
  await page.fill("#confirm", "password123");
  await page.click("button[type='submit']");
  await expect(page.locator("#message")).toContainText("Registration successful");

  // wrong password login
  await page.goto("/static/login.html");
  await page.fill("#email", email);
  await page.fill("#password", "wrongpassword");
  await page.click("button[type='submit']");

  await expect(page.locator("#message")).toContainText("Invalid credentials");
});
