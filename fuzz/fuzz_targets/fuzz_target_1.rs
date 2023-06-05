#![no_main]
use libfuzzer_sys::fuzz_target;
use changeme_bin::add;

fuzz_target!(|data: &[u8]| {
    let n1 = data.iter().map(|n| *n as u128).sum::<u128>() as u128;

    assert_eq!(add(n1, n1), n1 * 2);
});
