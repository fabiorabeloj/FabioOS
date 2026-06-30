import { chromium } from "playwright";

const browser = await chromium.launch();
const page = await browser.newPage();
const errors = [];
page.on("console", (m) => {
  if (m.type() === "error") errors.push(m.text());
});
page.on("pageerror", (e) => errors.push(e.message));

await page.goto("http://127.0.0.1:5174/", {
  waitUntil: "networkidle",
  timeout: 30000,
});
await page.waitForTimeout(4000);

const names = await page.locator(".agent-list strong").allTextContents();
const avatars = await page.locator(".avatar strong").count();
const banner = await page.locator(".banner--error").textContent().catch(() => null);

console.log("LIST_NAMES:", JSON.stringify(names));
console.log("AVATAR_COUNT:", avatars);
console.log("ERROR_BANNER:", banner ?? "none");
console.log("CONSOLE_ERRORS:", JSON.stringify(errors));

await browser.close();
process.exit(names.length === 5 && avatars === 5 ? 0 : 1);
