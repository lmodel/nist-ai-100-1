package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A positive, negative, or both consequence of an AI system. Impacts
can manifest as opportunities (positive) or threats (negative).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Impact extends NamedThing {

  private String impactSign;
  private String magnitude;
  private Float likelihood;
  private List<NamedThing> affects;


}