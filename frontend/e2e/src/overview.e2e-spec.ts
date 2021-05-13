import { browser, logging } from 'protractor';
import { OverviewPage } from './overview.po';

describe('Overview Page', () => {
  let page: OverviewPage;

  beforeEach(() => {
    page = new OverviewPage();
  });

  it('should display the correct energy sum', async () => {
    await page.navigateTo();
    expect(await page.getEnergySum()).toEqual('816.34 W');
  });

  it('should display 2 producers', async () => {
    await page.navigateTo();
    expect((await page.getProducers()).length).toBe(2);
  });

  it('should display the correct value of the first producer', async () => {
    await page.navigateTo();
    expect(await page.getFirstProducerValue()).toEqual('2,360.2 W');
  });

  it('should display 2 storages', async () => {
    await page.navigateTo();
    expect((await page.getStorages()).length).toBe(2);
  });

  it('should display 7 consumers', async () => {
    await page.navigateTo();
    expect((await page.getConsumers()).length).toBe(7);
  });

  afterEach(async () => {
    // Assert that there are no errors emitted from the browser
    const logs = await browser.manage().logs().get(logging.Type.BROWSER);
    expect(logs).not.toContain(jasmine.objectContaining({
      level: logging.Level.SEVERE,
    } as logging.Entry));
  });
});
