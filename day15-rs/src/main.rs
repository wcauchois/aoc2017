static DIVISOR: u64 = 2147483647;

#[derive(Debug)]
struct Generator {
    factor: u32,
    value: u32,
}

impl Generator {
    fn next(&mut self) {
        self.value = (((self.value as u64) * (self.factor as u64)) % DIVISOR) as u32;
    }

    fn rightmost_bits(&self) -> u32 {
        self.value & 0xffff
    }
}

fn main() {
    let mut gen_a = Generator {
        factor: 16807,
        value: 65,
    };
    let mut gen_b = Generator {
        factor: 48271,
        value: 8921,
    };
    let mut count: u32 = 0;
    for _ in 0..40000000 {
        if gen_a.rightmost_bits() == gen_b.rightmost_bits() {
            count += 1;
        }
        gen_a.next();
        gen_b.next();
    }
    println!("{}", count);
}
