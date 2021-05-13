import { browser, logging } from 'protractor';
import { ConfigurationsPage } from './configurations.po';

describe('Configurations Page', () => {
  let page: ConfigurationsPage;

  beforeEach(() => {
    page = new ConfigurationsPage();
  });

  it('should display the API url', async () => {
    await page.navigateTo();
    expect(await page.getApiUrl()).toEqual('http://localhost:5000/api');
  });

  it('should display the configurated activation threshold', async () => {
    await page.navigateTo();
    expect(await page.getBackendConfiguration()).toContain('activation_threshold: 200');
  });

  afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
      level: logging.Level.SEVERE,
    } as logging.Entry));
  });
});
