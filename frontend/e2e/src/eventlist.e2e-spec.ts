import { browser, logging } from 'protractor';
import { EventlistPage } from './eventlist.po';

describe('Eventlist Page', () => {
  let page: EventlistPage;

  beforeEach(() => {
    page = new EventlistPage();
  });

  it('should display the reload button', async () => {
    await page.navigateTo();
    expect(await page.getReloadButtonText()).toEqual('autorenew Reload');
  });

  afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
      level: logging.Level.SEVERE,
    } as logging.Entry));
  });
});
