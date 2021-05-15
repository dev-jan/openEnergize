import { browser, logging } from 'protractor';
import { AboutPage } from './about.po';

describe('About Page', () => {
  let page: AboutPage;

  beforeEach(() => {
    page = new AboutPage();
  });

  it('should display licenses links', async () => {
    await page.navigateTo();
    const links = await page.getLicenseLinks();
    expect(links.length).toBe(3);
    expect(links).toContain('https://fontawesome.com/');
    expect(links).toContain('https://picsum.photos/');
  });

  afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
      level: logging.Level.SEVERE,
    } as logging.Entry));
  });
});
