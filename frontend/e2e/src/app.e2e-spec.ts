import { browser, logging } from 'protractor';
import { AppPage } from './app.po';

describe('App Root', () => {
  let page: AppPage;

  beforeEach(() => {
    page = new AppPage();
  });

  it('should display correct title', async () => {
    await page.navigateTo();
    expect(await page.getTitleText()).toEqual('OpenEnergize');
  });

  it('should display all navigation entries', async () => {
    await page.navigateTo();
    expect((await page.getNavigationEntries()).length).toBe(4);
  });

  afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
      level: logging.Level.SEVERE,
    } as logging.Entry));
  });
});
