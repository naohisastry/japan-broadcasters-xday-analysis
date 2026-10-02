import asyncio
from playwright.async_api import async_playwright
import os

async def capture_thumbnail():
    target_html = r"file:///C:/Users/naohi/.gemini/antigravity/scratch/Japan_Broadcasters_XDay_Publish/index.html"
    output_png = r"C:\Users\naohi\.gemini\antigravity\scratch\Japan_Broadcasters_XDay_Publish\social-preview.png"
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        # 1200x630 is the recommended size for OGP (Twitter Card / Facebook)
        page = await browser.new_page(viewport={"width": 1200, "height": 800})
        
        print(f"Loading {target_html}...")
        await page.goto(target_html)
        
        # Wait for Chart.js animations to finish rendering
        await page.wait_for_timeout(3000)
        
        print(f"Saving screenshot to {output_png}...")
        # Crop exactly to 1200x630 for standard OGP aspect ratio
        await page.screenshot(
            path=output_png, 
            clip={"x": 0, "y": 0, "width": 1200, "height": 630}
        )
        
        await browser.close()
        print("Thumbnail captured successfully.")

if __name__ == "__main__":
    asyncio.run(capture_thumbnail())
